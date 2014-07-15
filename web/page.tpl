<!DOCTYPE html>
<html>
<head>
	<title>Super Secret Web Page</title>
	<link rel="stylesheet" type="text/css" href="/static/css/main.css"/>
</head>
<body>
	<img id="centre" src="/static/img/96d875aa-9dde-4ee4-b770-88675b415c59.svg" alt="something"/>
	<div id="grid">
%for imgSet in imageGrid:
	<div class="row">
%	for imgPath in imgSet:
		<img src="/static/img/{{imgPath}}" alt="something"/>
%	end
	</div>
%end
	</div>
</body>
</html>
