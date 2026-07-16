[reference](https://aws.amazon.com/blogs/database/managing-postgresql-users-and-roles/)
# recommended approach to fine grained access control

![Pasted image 20260716142915.png](app://88d7adeb3caf35ad6ef46ba14a60fc494dab/Users/chin/papers-please/Pasted%20image%2020260716142915.png?1784183355035)

- use master user to create roles for each use case (eg: `readonly`, `readwrite`)
- add permissions to allow roles to access database objects
	- eg: `readonly` role can only run `SELECT` queries
	- grant roles **the least possible permissions required** for the functionality
- create new users for each distinct functionality 
	- eg: `app_user`, `reporting_user`
- assign the role to each user 
	- eg: assign `readwrite` role to `app_user`; assign `readonly` to `reporting_user`!=! 
# users groups and roles
Users, groups and roles are the same thing in postgres; only difference is that users can login by default 

> [!NOTE] CREATE USER 
> CREATE USER = CREATE ROLE + GRANT LOGIN PERMISSION

to create a user: `CREATE USER myuser WITH PASSWORD 'supersecret'`
this is functionally equivalent to `CREATE ROLE myuser with LOGIN PASSWORD 'supersecret'`

# public schema and public role
when a new database is created, pg by default creates a schema called `public` and grants access on this schema to a backend role called `public`

all new users by default are granted the `public` role and can access/create objects inside the public schema ^5853d2

## search paths
pg uses a `search path` which is a list of schema names that pg checks when you don't use a fully qualified name

eg: if i `select * from mytable`, pg will look for `mytable` in the schemas listed in the search path. **by default**, the search path contains the following schemas:

```sql
postgres=# show search_path;
   search_path   
-----------------
 "$user", public
(1 row)
```

`$user` resolves to the name of the currently logged in user - by default, no schema exists that matches this username. this means that the `public` schema becomes the default schema used when no schema is specified. this is problematic because [[#^5853d2|all new users can readwrite to this schema]],  

hence, we need to revoke the default create permission on `public` schema from the `public` role to get a real `readonly` role: 
```sql
REVOKE CREATE ON SCHEMA public FROM PUBLIC;
```

this still preserves the ability of new users to login - we need to 

```sql
REVOKE ALL ON DATABASE mydatabase FROM PUBLIC;
```

This makes sure that users can’t connect to the database by default unless this permission is explicitly granted.


> [!NOTE] Revoking perms from `public`
> Any change to the `public` role impacts **all** existing users and roles (as they are [[#^5853d2|granted the public role by default]])
> 
> We should create a replacement role and give all existing users this role prior to revoking permissions

# creating database roles
## readonly role

1. we can first create a new role called `readonly`:
	- `CREATE ROLE readonly`
2. grant it the ability to `CONNECT` (basically a user at this point)
	- `GRANT CONNECT ON DATABASE mydb TO readonly`
3. grant the role usage access to your schema:
	- `GRANT USAGE ON SCHEMA myschema TO readonly`
4. grant access on all tables/views:
	- `GRANT SELECT ON ALL TABLES IN SCHEMA myschema TO readonly;`


> [!NOTE] GRANT SELECT
> Grant select is a **point in time operation** meaning that any new table creation in the future might not be accessible 
> 
> to circumvent this, you must do the following: 
> ```sql
> ALTER DEFAULT PRIVILEGES IN SCHEMA myschema GRANT SELECT ON TABLES TO readonly;
> ```

## readwrite role 
1. create role
2. grant role permission to connect
3. grant schema usage privilege 
	- if you want to allow the role to create new objects, need to do:
```sql
GRANT USAGE, CREATE ON SCHEMA myschema TO readwrite;
```
4. grant access to tables:
	- individual tables:
```sql
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA myschema TO readwrite;
```

if want to grant to all tables: 
```sql
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA myschema TO readwrite;
```

to automatically grant permissions on tables + views added in the future: 
```sql
ALTER DEFAULT PRIVILEGES IN SCHEMA myschema GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO readwrite;
```


> [!NOTE] Sequences
> read/write roles also need to be able to use sequences; can grant selective access using
> ```sql
> GRANT USAGE ON SEQUENCE myseq1, myseq2 TO readwrite;
> ```
> 
> for granting full access:
> ```sql
> GRANT USAGE ON ALL SEQUENCES IN SCHEMA myschema TO readwrite;
> ```
> 
> for future access:
> ```sql
> ALTER DEFAULT PRIVILEGES IN SCHEMA myschema GRANT USAGE ON SEQUENCES TO readwrite;
> ```

# Creating users
once the roles are up, creating userse is easy:
```sql
CREATE USER myuser1 WITH PASSWORD 'secret_passwd';
GRANT readonly TO myuser1;
```

