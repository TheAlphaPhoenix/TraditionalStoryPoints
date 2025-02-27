<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Story Points Calculator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            text-align: center;
            padding: 20px;
        }
        .container {
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            max-width: 600px;
            margin: auto;
        }
        select, button {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            font-size: 16px;
        }
        .result {
            font-size: 20px;
            font-weight: bold;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Story Points Calculator</h1>
        <p>Select values for each category:</p>
        
        <label>Technical Complexity</label>
        <select id="technicalComplexity">
            <option value="1">Low</option>
            <option value="2">Medium</option>
            <option value="3">High</option>
        </select>

        <label>Integration Complexity</label>
        <select id="integrationComplexity">
            <option value="1">Low</option>
            <option value="2">Medium</option>
            <option value="3">High</option>
        </select>

        <label>Implementation Effort</label>
        <select id="implementationEffort">
            <option value="1">Low</option>
            <option value="2">Medium</option>
            <option value="3">High</option>
        </select>

        <label>Testing Effort</label>
        <select id="testingEffort">
            <option value="1">Low</option>
            <option value="2">Medium</option>
            <option value="3">High</option>
        </select>

        <label>Uncertainty</label>
        <select id="uncertainty">
            <option value="1">Low</option>
            <option value="2">Medium</option>
            <option value="3">High</option>
        </select>

        <button onclick="calculateStoryPoints()">Calculate Story Points</button>
        <div class="result" id="storyPointsResult">Story Points: 0</div>
    </div>

    <script>
        function calculateStoryPoints() {
            const fibonacci = [1, 2, 3, 5, 8, 13, 21];
            
            let totalScore =
                parseInt(document.getElementById('technicalComplexity').value) +
                parseInt(document.getElementById('integrationComplexity').value) +
                parseInt(document.getElementById('implementationEffort').value) +
                parseInt(document.getElementById('testingEffort').value) +
                parseInt(document.getElementById('uncertainty').value);
            
            let storyPoints = fibonacci.find(num => num >= totalScore) || 21;
            
            document.getElementById('storyPointsResult').innerText = `Story Points: ${storyPoints}`;
        }
    </script>
</body>
</html>
