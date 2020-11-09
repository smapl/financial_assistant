function registrtion() {
  let resg_url = "http://0.0.0.0:5000/identification/registration";

  let login = document.querySelector(".login").value;
  let password = document.querySelector(".password").value;
  let fname = document.querySelector(".fname").value;
  let lname = document.querySelector(".lname").value;
  let email = document.querySelector(".email").value;
  let date_of_birth = document.querySelector(".date_of_birth").value;

  let data_to_server = {
    login: login,
    password: password,
    fname: fname,
    lname: lname,
    date_of_birth: date_of_birth,
    email: email,
  };
  axios
    .post(resg_url, data_to_server, {
      headers: { "content-type": "application/json" },
    })
    .then((response) => {
      console.log(response.data);
      if (response.status == 200) {
        if (response.data["result"] == true) {
          alert("User success registration");
        } else {
          alert(response.data["result"]);
        }
      } else {
        console.log(response.status);
      }
    })
    .catch((error) => {
      console.log(error);
    });
}

function login() {
  let log_url = "http://0.0.0.0:5000/identification/login";
  let check_login = document.querySelector(".check_login").value;
  let check_password = document.querySelector(".check_password").value;
  let data_to_check = {
    login: check_login,
    password: check_password,
  };

  axios
    .post(log_url, data_to_check, {
      headers: { "content-type": "application/json" },
    })
    .then((response) => {
      if (response.status == 200) {
        res = response.data;
        if (res["result"] == true) {
          console.log(res["redirect_url"]);
          window.location.href = res["redirect_url"];
        } else {
          console.log(res["result"]);
        }
      }
    })
    .catch((error) => {
      console.log(error);
    });
}

document.getElementById("reg").addEventListener("click", registrtion);

document.getElementById("log").addEventListener("click", login);
