const fs = require("fs");

function signup(user, email, passwd) {
  let jsondata = JSON.parse(fs.readFileSync("data.json"));
  
  if (!jsondata.hasOwnProperty("user")) {
    jsondata.user = {};
  }

  newData = {name: user,email: email,passwd: passwd};
  jsondata.user = newData;
  
  fs.writeFileSync("data.json", JSON.stringify(jsondata));
};

signup('segxx','fuckme@gmail.com','bbc');