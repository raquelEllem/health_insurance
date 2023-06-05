// PA004 Health Insurance Cross-sell
function onOpen() {
  var ui = SpreadsheetApp.getUi();
  ui.createMenu('Health Insurance Prediction')
    .addItem('Get Prediction', 'PredictAll')
    .addToUi();  
}

// Production Server
const host_production = 'health-insurance-api-amhg.onrender.com'

// ----------------------------
// ----- Função Auxiliar ------
// ----------------------------
// Chamada à API
function ApiCall(data, endpoint) {
  const url = 'https://' + host_production + endpoint;
  const payload = JSON.stringify(data);

  const options = {
    method: 'POST',
    contentType: 'application/json',
    payload: payload
  };

  var response = UrlFetchApp.fetch(url, options);

  // obter resposta
  var rc = response.getResponseCode();
  var responseText = response.getContentText();

  if (rc !== 200) {
    Logger.log('Resposta (%s) %s', rc, responseText);
  } else {
    prediction = JSON.parse(responseText);
  }
  return prediction;
}


// Health Insurance Propensity Score Prediction
function PredictAll() {
  // parâmetros do Google Sheets
  var ss = SpreadsheetApp.getActiveSheet();
  var titleColumns = ss.getRange('B2:M2').getValues()[0];
  var lastRow = ss.getLastRow();

  var data = ss.getRange(`B3:M${lastRow}`).getValues();

  // percorrer todas as linhas
  for (let row in data) {
    const json = {};

    // percorrer todas as colunas
    for (let j = 0; j < titleColumns.length; j++) {
      json[titleColumns[j]] = data[row][j];
    }

    // arquivo JSON para enviar
    const json_send = {
      id: json['id'],
      gender: json['gender'],
      age: json['age'],
      driving_license: json['driving_license'],
      region_code: json['region_code'],
      previously_insured: json['previously_insured'],
      vehicle_age: json['vehicle_age'],
      vehicle_damage: json['vehicle_damage'],
      annual_premium: json['annual_premium'],
      policy_sales_channel: json['policy_sales_channel'],
      vintage: json['vintage'],
      response: json['response']
    };

    // Pontuação de propensão
    pred = ApiCall(json_send, '/predict');

    /// Enviar de volta para o Google Sheets
    var score = pred[0]['score']; // Obter o valor do score sem arredondamento
    var cell = ss.getRange(Number(row) + 3, 13);
    cell.setNumberFormat("0.##############"); // Define o formato da célula para exibir todos os números decimais
    cell.setValue(score);

    
    // Adicionar formatação condicional para linhas com score acima de 0.02
    if (score > 0.02) {
      cell.setBackground("#FFA07A"); // Rosa salmão
    }
  }

  // Reorganizar a tabela com base no score em ordem decrescente
  var range = ss.getRange(`B3:M${lastRow}`);
  range.sort({ column: 13, ascending: false });

}