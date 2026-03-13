7<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Tabela Sistemas Operacionais</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            padding: 20px;
            background: #ffffff;
        }

        table {
            width: 700px;
            margin: auto;
            border-collapse: collapse;
            text-align: center;
            background-color: #f7f7f7;
        }

        #primeiracoluna {
            width: 100px;
            text-align: left;
            padding-left: 10px;
        }

        .colunas {
            width: 120px;
        }

        th, td {
            border: 1px solid #ffffff;
            padding: 8px;
        }

        th:nth-child(1) {
            background-color: #f2f2f2;
            border-top: px solid #999;
        }

        th:nth-child(2) {
            background-color: #d6f5d6;
            border-top: 3px solid #99cc00; /* Android */
        }

        th:nth-child(3) {
            background-color: #d6e5ff;
            border-top: 3px solid #6699ff; /* iOS */
        }

        th:nth-child(4) {
            background-color: #e5d6f5;
            border-top: 3px solid #9966cc; /* Windows Phone */
        }

        th:nth-child(5) {
            background-color: #ffe5d6;
            border-top: 3px solid #ff9933; /* Others */
        }

        td:first-child,
        td:first-child{
       font-weight: bold;

        }
    </style>
</head>
<body>
    <table>
        <tr>
            <th id="primeiracoluna">Period</th>
            <th class="colunas">Android</th>
            <th class="colunas">iOS</th>
            <th class="colunas">Windows Phone</th>
            <th class="colunas">Others</th>
        </tr>
        <tr>
            <td>2016Q1</td>
            <td>83.4%</td>
            <td>15.4%</td>
            <td>0.8%</td>
            <td>0.4%</td>
        </tr>
        <tr>
            <td>2016Q2</td>
            <td>87.6%</td>
            <td>11.7%</td>
            <td>0.4%</td>
            <td>0.3%</td>
        </tr>
        <tr>
            <td>2016Q3</td>
            <td>86.8%</td>
            <td>12.5%</td>
            <td>0.3%</td>
            <td>0.4%</td>
        </tr>
        <tr>
            <td>2016Q4</td>
            <td>81.4%</td>
            <td>18.2%</td>
            <td>0.2%</td>
            <td>0.2%</td>
        </tr>
        <tr>
            <td>2017Q1</td>
            <td>85.0%</td>
            <td>14.7%</td>
            <td>0.1%</td>
            <td>0.1%</td>
        </tr>
    </table>
</body>
</html>
