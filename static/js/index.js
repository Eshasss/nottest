function onRegisterButtonClick() {
  const name1 = document.getElementById("user_name").value;
  const password2 = document.getElementById("user_password").value;
  const url = "http://127.0.0.1:8000/profile/";
  console.log(name1, password2)
    fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin":  "no-cores "
      },
      body: JSON.stringify({
        name: name1,
        password: password2,
      }),
    })
    .then((response) => response.text())
    .then((text) => JSON.parse(text))
    .then((json) => json.user_id)
    //.then((user_id) sole.l=> sessionStorage.setItem("user_id", user_id.toString()))
    .catch((error) => console.log(error));

    //window.location.replace("http://localhost:8000/end/");
  }
