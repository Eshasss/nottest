function onRegisterButtonClick() {
  const name = document.getElementById("user_name").value;
  const password = document.getElementById("user_password").value;
  const url = "http://127.0.0.1:8000/newguy/";
  console.log(name, password)
  fetch(url, {
    method: "POST",
    headers: {
    "Content-Type": "application/json",
    },
    body: JSON.stringify({
      name: name,
      password: password,
     }),
  })
  .then((response) => response.text())
  .then((text) => JSON.parse(text))
  .then((json) => json_response = json)
  .catch((error) => console.log(error))
  //window.location.replace("http://localhost:8000/end/");
  }


function onLoginButtonClick() {
  var status
  var password
    const name = document.getElementById("user_name").value;
    const password = document.getElementById("user_password").value;
    const url = "http://127.0.0.1:8000/oldguy/";
    console.log(name, password)
    fetch(url, {
      method: "POST",
      headers: {
      "Content-Type": "application/json",
      },
      body: JSON.stringify({
        name: name,
        password: password,
       }),
    })
      .then((response) => {
        status = response.status_code;
        return response.text();
      })
    .then((text) => JSON.parse(text))
      .then((json) => {
        password_correct = json.password
        if (status != 200) {
          alert("lox")
        }
        if (password_correct == password) {
          alert("ne lox")
        }
    })
    .catch((error) => console.log(error))
    //window.location.replace("http://localhost:8000/end/");
    }