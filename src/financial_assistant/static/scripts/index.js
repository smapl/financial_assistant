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
  console.log(data_to_server);
  axios.post(resg_url, data_to_server).then(function (response) {
    console.log(response.data);
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

  let res = send_req(log_url, data_to_check);

  if ((res != false) & (res != undefined)) {
    if (res["result"] == true) {
      console.log(res["redirect_url"]);
      window.location.href = res["redirect_url"];
    } else {
      console.log(res["result"]);
    }
  } else {
    console.log(res);
  }
}

function send_req(req_url, params) {
  axios
    .post(req_url, params, { headers: { "content-type": "application/json" } })
    .then((response) => {
      if (response.status == 200) {
        return response.data;
      } else {
        return false;
      }
    })
    .catch((error) => {
      console.log(error);
    });
}
