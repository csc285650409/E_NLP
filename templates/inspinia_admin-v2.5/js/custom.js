$(document).ready(function(){
	baseUrl = 'http://127.0.0.1:8000/';
	//$('.summernote').summernote();
	//$('.note-editable').summernote('code', "123123");
	console.log($('.summernote').code());
					 $('.summernote').code("12313");
					 $('#editText').val("123123123123");
	$("#saveBtn").click(function(){
		var text = $(".note-editable").text();
		//console.log(text);
		$.ajax({
				url:baseUrl+'save/',
				type:'POST',
				data:{'text':text},
				async:true,
				success:function(data){
					console.log(data);
				}
			})
	});

	$("#uploadBtn").click(function(){
		var file = $('<input type=\'file\' name=\'file\' id=\'files\'/>');
		var form = $('<form></form>');
		file.appendTo(form);
		file.click();
		file.change(function(){
			var fromData = new FormData(form[0]);
			$.ajax({
				url:baseUrl+'file/',
				type:'POST',
				data:fromData,
				async:true,
				cache: false,   
            contentType: false, //不设置内容类型  
            processData: false, //不处理数据  
				success:function(data){
					try{
					 var a = data.text;
					 $('.summernote').code(a);
					}catch(e){
						console.log(e);
					}
				}
			})
		});
	});
})