<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Medical Analysis</title>
    <style>
        body {
            text-align: center;
            font-family: Arial;
            background-color: #f0f8ff;
        }
        .container {
            margin-top: 30px;
        }
        img {
            width: 200px;
            margin: 10px;
            border-radius: 15px;
        }
        .link {
            display: inline-block;
            margin-top: 30px;
            padding: 15px 25px;
            background: blue;
            color: white;
            text-decoration: none;
            border-radius: 5px;
        }
    </style>
</head>
<body>

<h1>Medical Analysis</h1>

<div class="container">
    <img src="{{ url_for('static', filename='images/nursing_home.jpg') }}">
    <img src="{{ url_for('static', filename='images/hospital.jpg') }}">
    <img src="{{ url_for('static', filename='images/disease.png') }}">
    <img src="{{ url_for('static', filename='images/health.png') }}">
</div>

<a class="link" href="{{ url_for('map_view') }}">
    View Disease Analysis Map
</a>

</body>
</html>
