function onRegisterButtonClick() {
    var status
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
        .then((response) => {
          status = response.status;
          return response.text();
        })
      .then((text) => JSON.parse(text))
      .then((json) => {
        console.log("D", status)
        if (status == 200) {
          console.log("dsdsds", status);
          window.location.replace("http://localhost:8000/test/");
              
        } else {
          console.log("smthswo", status);
          var text = document.getElementById("ErrorText");
          text.style.display = "block";
            
        }})
      .catch((error) => console.log(error))

      }