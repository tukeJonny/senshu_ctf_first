'use strict'
$(document).ready(function(){
  $("#submit-flag").on("click",function(){
	submit();
  });
});

const accept = 1
const bad = 2
const already = 3

function submit(){
	if(! $.isNumeric($("#problem-id").attr('class'))){
		console.error("invalid problem id");
		return false;
	}	
	let id = parseInt($("#problem-id").attr('class'))
	let flag = $("#flag-text").val()
	let csrf = $("[name='csrfmiddlewaretoken']").val()
	return $.ajax({
		type:"POST",
		url:"/scoreserver/submit/"+id+"/",
		data:"flag="+flag+"&csrfmiddlewaretoken="+csrf,
	}).then(function(data){
		console.log(data)
		judge(data.status);
		$("#result-message").text(data.message);
		$("#flag-result").modal("toggle");
	},function(data){
		console.log("ajax fail");
		$("#result-message").text("sorry,ajax request fail :/            Please report admin.");
		$("#result-color").removeClass();
		$("#result-color").addClass("modal-content panel-danger");
		$("#modal-head").text("Connection Error");
		$("#flag-result").modal("toggle");
	});
}

function judge(status){
	switch(status){
		case accept:
			console.log("congratz");
			$("#result-color").removeClass();
			$("#result-color").addClass("modal-content panel-success");
			$("#modal-head").text("Congrats");
			break;
		case bad:
			console.log("but flag");
			$("#result-color").removeClass();
			$("#result-color").addClass("modal-content panel-danger");
			$("#modal-head").text("uhhhhhhhh");
			break;
		case already:
			console.log("already solve");
			$("#result-color").removeClass();
			$("#result-color").addClass("modal-content panel-warning");
			$("#modal-head").text("ah?");
			break;
	}
}

	
