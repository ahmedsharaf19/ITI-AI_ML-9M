// 1.	Create a Database named "ITI_Mongo".
use ITI_Mongo

// 2.	Create a Collection named "Staff".
// 3.	Insert one document into the "Staff" collection: {_id, name, age, gender, department}.
db.Staff.insertOne({name:"Ahmed", age:23, gender:"male", department:"AI"})

// 4.	Insert many documents into the "Staff" collection:
// Object: {_id, name, age: 20, gender: "male", department}
// Object: {_id, name, age: 25, gender: "female", managerName, department}
// Object: {_id, name, age: 15, gender, DOB}
db.Staff.insertMany([
    {name:"Mohamed", age:20, gender:"male", department:"CS"},
    {name:"Mona", age:25, gender:'female', managerName: "Sharaf", department:"IT"},
    {name:"Ali", age:15, gender:"male", DOB:"K1"}
])

// 5.	Query to find data from the "Staff" collection:
//     1) Find all documents.
db.Staff.find({})

//     2) Find documents where gender is "male".
db.Staff.find({gender:"male"})

//     3) Find documents with age between 20 and 25.
db.Staff.find({"age":{$lte:25, $gte:20}})

//     4) Find documents where age is 25 and gender is "female".
db.Staff.find({$and: [{age:25}, {gender:"female"}]})

//     5) Find documents where age is 20 or gender is "female".
db.Staff.find({$or: [{age: 20}, {gender:'female'}]})

// 6.	Update one document in the "Staff" collection where age is 15, set the name to "your name".
db.Staff.updateOne({age: 15}, {$set:{name:"Ahmed Sharaf"}})
db.Staff.find({})

// 7. Update many documents in the "Staff" collection, update the department to "AI".
db.Staff.updateMany({}, {$set:{department:"AI"}})
db.Staff.find({})

// 8.	Create a new collection called "test" and insert documents from Question 4.
db.test.insertMany([
    {_id:ObjectId(), name:"Mohamed", age:20, gender:"male", department:"CS"},
    {_id:ObjectId(), name:"Mona", age:25, gender:'female', managerName: "Sharaf", department:"IT"},
    {_id:ObjectId(), name:"Ali", age:15, gender:"male", DOB:"K1"}
])
db.test.find({})

// 9.	Try to delete one document from the "test" collection where age is 15.
db.test.deleteOne({age: 15})
db.test.find({})

//    a.	With justification, explain which document will be deleted if more than one has age = 15. (Try it.)
db.test.insertMany([
{_id: 10, name: "Khalid", age: 15, gender:"male", department:"ai"},
{_id: 11, name: "mousa", age: 15, gender:"male", department:"cs"},
{_id: 12, name: "samir", age: 15, gender:"male", department:"it"}
])
db.test.find({})
db.test.deleteOne({age: 15})  // it will delete first document will matched
db.test.find({})

//    b.	First insert: db.collection.insertOne({ _id: 5, name: "ahmed", age: 15 })
db.test.insertOne({_id:5, name:"ahmed", age:15})

//    c.	Second insert: db.collection.insertOne({ _id: 6, name: "eman", age: 15 })
db.test.insertOne({_id:6, name:"eman", age:15})

//    d.	b. When you run deleteOne, will it delete ahmed or eman?
db.test.deleteOne({age: 15}) // it will delete ahmed

// 10. try to delete all male gender
db.test.deleteMany({gender:"male"})
db.test.find({})

// 11. Try to delete all documents in the "test" collection.
db.test.drop()