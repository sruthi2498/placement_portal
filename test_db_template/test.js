function validate(){

	var username=GetUsernameFromForm();
	var password=GetPasswordFromForm();
	document.getElementsByTagName('div')[2].innerHTML="";
	if(username==null || username==""){
		document.getElementsByTagName('div')[2].innerHTML="Enter USN";
		return false;
	}
	if (password == null || password == "") {
	   	document.getElementsByTagName('div')[2].innerHTML="Enter password";
		return false;
	}
	
	else{
		
		$.post(
			"http://ppdb-ep.herokuapp.com/login",
			{
				"usn": username,
				"email" : "kys",
				"password" : password
			},
			function (data) {
				console.log("sdsd",data)
		//	if(!err) {
				if(data==true){
					console.log("sdsd")
					/*


						Do
						Some 
						UI stuff
						here
						like 
						 |	
						 |
						 |
						\ /	
						 |	
					*/
					document.getElementsByTagName('div')[2].innerHTML="Done go";
		//		}
				}	
				else console.log(err);
			});
		return false;
	}

}

function GetUsernameFromForm(){
	//Edit this based on DOM structure
	return document.forms["details"]["usn"].value;
}
function GetPasswordFromForm(){
	//Edit this based on DOM structure
	return document.forms["details"]["pass"].value;
}