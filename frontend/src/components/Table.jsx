import TableRow from "./TableRow"

function Table( {data} ) {

  return (
      <table>
        <thead>
          <tr>
            <th>id ordine</th>
            <th>anno</th>
            <th>stato</th>
            <th>nome</th>
            <th>cognome</th>
          </tr>
        </thead>
        <tbody>
          { data.map( (x, i) => <TableRow ordini={x} key={i} /> ) }
        </tbody>
      </table>
  )
  
}

export default Table