
const MongoClient = require('mongodb').MongoClient;
const uri = "mongodb+srv://tampier:tampier@cluster0.wybmf.mongodb.net/ecotag?retryWrites=true&w=majority";
const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });
client.connect(err => {
  const collection = client.db("ecotag").collection("events");
  
  client.close();
});




