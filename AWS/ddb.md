---
id: ddb
aliases: []
tags: []
---

# concepts 
#ddb

- **table** - collection of data 
- **items** - uniquely identifiable group of attributes 
	- each item needs to have a unique item id 
	- this item id could be a combination of attributes
- **attributes** - fundamental unit of data; cannot be broken down further  


> [!NOTE] nested items
> note that each table can contain a nested group of items! ie, `A (table) -> B (item) -> C (item) -> D (attr)` is perfectly valid

## items

- 2 forms of pkey 
	- partition key: used for physical storage
	- partition + sort keys: partition key same as above, sort key is within partition 

# data streams 

- ddb optional feature that does cdc whenever something is edited on the table 
	- new item add 
	- item update
	- item delete 

# ddb consistency guarantees 
#consistency 

-  anything using the same partition key as the table can have **strongly consistent reads** 
	- this is local secondary indexes (LSI) + table items itself 
- writes that have been ACK-ed are durable. 
- NOTE: what happens if i rename a folder with concurrent write to a file in the folder? 