1. we have to create permissions that allow a specific **IAM user** to connect to a **RDS user**
2. we have to create specific DB role that has `rds_iam` and attach it to the afore-mentioned RDS user 
3. this allows the pg user to auth using sso 
	1. however, we still need to `REQUIRE` tls in order to use rds iam
