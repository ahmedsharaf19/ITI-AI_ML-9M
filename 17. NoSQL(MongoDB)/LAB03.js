use ITI_Mongo

// 1.	Provide the MongoDB code for enforcing JSON schema validation 
// when creating a collection named "employees"
// with required fields "name," "age" (min. 18), 
// and "department" (limited o ["HR," "Engineering," "Finance"]).

db.createCollection("employees", {
    validator: {
        $jsonSchema: {
            bsonType: "object",
            title: "Must Contain Name, age, dep",
            required: ['name', 'age', 'department'],
            properties: {
             "age": {
                 bsonType: ["double", "int"],
                 description: "age must be numerical and start from 18",
                 minimum: 18
             },
             "department": {
                 bsonType: "string",
                 description:"Department must be text",
                 "enum": ["HR", "Engineering", "Finance"]
             }   
            }
        }
    }
})

db.employees.insertOne({name: "ahmed", age: 10, department: "HR"})
db.employees.insertOne({name: "ahmed", age: 20, department: "CS"})
db.employees.insertOne({name: "ahmed", age: 30, department: "HR"})

// 2.	Create new Database named Demo 
use Demo

// And Collections named trainningCenter1, trainningCenter2 
db.createCollection("trainningCenter1")
db.createCollection("trainningCenter2")

// a.	Insert documents into trainningCenter1 collection contains (Use Variable named data as Array)
//     i.	_id , name as firstName lastName , age , address, status as array 
data = [
    {_id: 1, firstName: "Ahmed", lastName: "Sharaf", age: 23, address: "zag", status: "single"},
    {_id: 2, firstName: "Samir", lastName: "Ahmed", age: 30, address: "cairo", status: "Married"},
]
// b.	Using insert ONE from data Variable
db.trainningCenter1.insertOne(data)
db.trainningCenter1.find({}) // added as two different field
// c.	Using Same Variable (data) with same data and insert MANY into trainningCenter2 collection
db.trainningCenter2.insertMany(data)
db.trainningCenter2.find({})

// 3.	Use find. explain function (find by age field) and mention scanning type
db.trainningCenter1.find({age: 23}).explain() // COLLSCAN


// 4.	Create index on created collection named it “IX_age” on age field 
db.trainningCenter1.createIndex({age: 1}, {name: "IX_age"})

// 5.	Use find. explain view winning plan for index created (find by age field) and mention scanning type
db.trainningCenter1.find({age: 23}).explain() // IXSCAN

// 6.	Create index on created collection named it “compound” on firstNsme and lastName
db.compound.insertMany([
    {_id:1, fName: "Ahmed", lName: "Sharaf", dep: "AI"},
    {_id:2, fName: "samir", lName: "ali", dep: "cs"},
    {_id:3, fName: "ali", lName: "khalid", dep: "hr"},
    {_id:4, fName: "khalid", lName: "osama", dep: "AI"},

])
//     a.	Try find().explain before create index and mention scanning type
db.compound.find({fName: "Ahmed", lName: "Sharaf"}).explain() // COLLSCAN
//     b.	Try find().explain after create index and mention scanning type
db.compound.createIndex({fName: 1, lName: 1}, {name: "full name"})
db.compound.find({fName: "Ahmed", lName: "Sharaf"}).explain() // IXSCAN

// 7.	Drop Demo Database
db.dropDatabase()


// Bouns
// 1.	Use mongodump to back up your Lab database.
// mongodump --db Demo --out "H:\ITI-AI_ML-9M\17. NoSQL(MongoDB)"

// 2.	Drop the Lab database.
db.dropDatabase()

// 3.	Use mongorestore to restore it with a new name: ITI_Course.
// mongorestore --db Demo --dir "H:\ITI-AI_ML-9M\17. NoSQL(MongoDB)\Demo"

use Demo