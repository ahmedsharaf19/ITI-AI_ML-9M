use ITI_Mongo

// 1.	Find documents where the "tags" field exists.
db.inventory.find({tags: {$exists: true}})

// 2.	Find documents where the "tags" field does not contain values "ssl" or "security."
db.inventory.find({tags: {$nin:["ssl", "security"]}})

// 3.	Find documents where the "qty" field is equal to 85.
db.inventory.find({qty: 85})

// 4.	Find documents where the "tags" array contains all of the values [ssl, security] using the `$all` operator.
db.inventory.find({
  tags: { $all: ["ssl", "security"] }
})

// 5.	Find documents where the "tags" array has a size of 3.
db.inventory.find({
  tags: { $size: 3 }
})

// 6.	Update the "item" field in the "paper" document, update "size.uom" to "meter" and using the `$currentDate` operator.
db.inventory.updateOne(
    { item: "paper" },
    {
        $set: { "size.uom": "meter" },
        $currentDate: { lastModified: true }, 
    },
);

//    a.	Also, use the upsert option (within updateOne)and change filter condition item:”laptopDevice”.
db.employees.updateOne( 
    { item: "laptopDevice" },
    {
        $set: { "size.uom": "meter" },
        $currentDate: { lastModified: true }, 
    },
    { upsert: true }
);

//    b.	Use the $setOnInsert operator to add new data if an insert occurs.
db.inventory.updateOne(
    { item: "paper" },
    {
        $set: { "size.uom": "meter" },
        $currentDate: {lastModified: true }, 
        $setOnInsert: {createdBy: "sharaf"}
    },
    { upsert: true }
);
//    Example field: dataSource: "todayRegister"
//    c.	Try using the updateMany operation.
db.inventory.updateMany(
    { item: "paper" },
    {
        $set: { "size.uom": "meter" },
        $currentDate: { lastModified: true }, 
        $setOnInsert: {createdBy: "sharaf"}
    },
    { upsert: true }
);
//    d.	Try using the `replaceOne` operation
db.inventory.replaceOne(
    { item: "paper" },
    {
        replaced: "true"
    },
    { upsert: true }
);

// 7.	Insert a document with incorrect field names "neme" and "ege," then rename them to "name" and "age."
db.inventory.insertOne({
    neme: "sharaf",
    ege: 24
});

db.inventory.find({neme : "sharaf"})

db.inventory.updateOne(
    {neme : "sharaf"}, 
    {
        $rename: {
            "neme": "name",
            "ege": "age"
        }
    }
);
db.inventory.find({name : "sharaf"})

// 8.	Try to reset any document field using the `$unset` function.
db.inventory.updateOne(
    { name: "sharaf" }, 
    {
        $unset: { age: "" }
    }
);

db.inventory.find({name : "sharaf"})

// 9.	Try update operators like `$inc`, `$min`, `$max`, and `$mul` to modify document fields.
// Important: Use a different field for each operation listed below. Insert Data If Not Existing
// Apply the following MongoDB update operators to the specified fields:
//    •	Use $max on the field: salary
//    •	Use $min on the field: overtime
//    •	Use $inc on the field: age
//    •	Use $mul on the fields: quantity and price
db.inventory.insertOne({
    name: "Ahmed",
    age: 24,
    salary: 5000
});

db.inventory.updateOne(
    { name: "Ahmed" },
    { $inc: { age: 1 } }
);

db.inventory.find({name : "Ahmed"})

db.inventory.updateOne(
    { name: "Ahmed" },
    { $min: { salary: 4000 } }
);

db.inventory.find({name : "Ahmed"})

db.inventory.updateOne(
    { name: "Ahmed" },
    { $max: { salary: 10000 } }
);

db.inventory.find({name : "Ahmed"})

// 10.	Calculate the total revenue for product from sales collection documents within the date range '01-01-2020' to '01-01-2023' 
// and then sort them in descending order by total revenue.
db.sales.aggregate([
{
  $match: {
    date: {
      $gte: ISODate("2020-01-01"),
      $lte: ISODate("2023-01-01")
    }
  }
},
{
  $group: {
    _id: "$product",
    totalRevenue: {
      $sum: { $multiply: ["$quantity", "$price"] }
    }
  }
},
{
  $sort: { totalRevenue: -1 }
}
])

// 11.	Calculate the average salary for employees for each department from the employee’s collection.
db.employees.aggregate([
{
  $group: {
    _id: "$department",
    avgSalary: { $avg: "$salary" }
  }
}
])

// 12.	Use likes Collection to calculate max and min likes per title
db.likes.aggregate([
                    {
                        $group: 
                        {
                            _id: "$title",
                            maxVal: { $max : "$likes"},
                            minVal: { $min : "$likes"},
                        }
                    },
                   
])