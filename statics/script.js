async function handleSubmit(event) {
  // annulla l'invio automatico del form, lo dovrò gestire io
  event.preventDefault()

  let citta = event.target[0].value
  let response = await fetch("/api/ordini/" + citta)
  let json = await response.json()

  populateTable(json)
}

function populateTable(json) {
  let html = ""

  if(json.length <= 0) {
    alert("NO DATA")
    return // ferma prima la funzione!!!
  }

  for(let x of json) {
    html += `
    <tr>
      <td>${x.username}</td>
      <td>${x.id}</td>
      <td>${x.data}</td>
    </tr>
    `
  }

  tbody.innerHTML = html
  table.style.display = "table"
}


function populateTableSafe(json) {
  tbody.innerHTML = ""

  for(let x of json) {
    tr = document.createElement("tr")
    td1 = document.createElement("td")
    td1.innerText = x.username
    td2 = document.createElement("td")
    td2.innerText = x.id
    td3 = document.createElement("td")
    td3.innerText = x.data
    tr.appendChild(td1)
    tr.appendChild(td2)
    tr.appendChild(td3)
    tbody.appendChild(tr)
  }
}