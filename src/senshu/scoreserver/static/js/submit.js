'use strict'
$(document).ready(function(){
  $("#submit-flag").on("click",function(){
	console.log("post");
	submit().done(function(data){
		console.log("ok");
		
	}).fail(function(data){
		console.log("fail");
	});
  });
});
const accept = 1
const bad = 2
const already = 3

function submit(){
	if(! $.isNumeric($("#problem-id").attr('class')[0])){
		console.error("invalid problem id");
		return false;
	}	
	let id = parseInt($("#problem-id").attr('class')[0])
	let flag = $("#flag-text").val()
	let csrf = $("[name='csrfmiddlewaretoken']").val()
	return $.ajax({
		type:"POST",
		url:"/scoreserver/submit/"+id+"/",
		data:"flag="+flag+"&csrfmiddlewaretoken="+csrf,
	})
}

function judge(status){
	switch(status){
		case accept:
			console.log("congratz");
			break;
		case bad:
			console.log("shit");
			break;
		case already:
			break;
	}
}

	
