function transport() {
  data = { module: true };
  axios.post("http://0.0.0.0:5000/handler", data).then((response) => {
    console.log(response.data);
    if ((response.data["result"] = true)) {
      window.location.href = response.data["redirect_url"];
    } else {
      console.log(response.data);
    }
  });
}
