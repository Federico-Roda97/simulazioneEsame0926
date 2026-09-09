

function TableRow( {ordini} ) {

  return (
    <tr>
      <td><i>{ordini.id_ordine}</i></td>
      <td>{ordini.anno}</td>
      <td>{ordini.stato}</td>
      <td>{ordini.nome}</td>
      <td>{ordini.cognome}</td>

    </tr>
  )

}

export default TableRow