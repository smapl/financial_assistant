url = "http://0.0.0.0:5000/personality/indent_user";
axios.get(url).then((response) => {
  let user = response.data["user_name"];
  document.write(user);
});
