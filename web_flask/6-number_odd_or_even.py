CTYPE html>
<HTML lang="en">
	<HEAD>
		<TITLE>HBNB</TITLE>
	</HEAD>
	<BODY>
		{% if number % 2 == 0 %}
			<h1>Number: {{ number }} is even</h1>
		{% else %}
			<h1>Number: {{ number }} is odd</h1>
		{% endif %}
	</BODY>
</HTML>

