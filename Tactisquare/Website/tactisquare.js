function play() {
	document.getElementById("menu").style.display = "none";
	username()
}

function username() {
	var user = document.getElementById("username").value
	console.log(user, "joined")
	const xhttp = new XMLHttpRequest();
	xhttp.open("PUT", "http://localhost:8000/players/0/0/0/0/"+user, true);
	xhttp.send();
}
