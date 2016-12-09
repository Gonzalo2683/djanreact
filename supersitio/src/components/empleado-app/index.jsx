import React from 'react'
import PostList from '../empleado-list/index'

class Posteos extends React.Component {

  constructor(props) {
    super(props)
    this.state = { empleados: [] }
  }

  componentWillMount() {
    fetch('http://127.0.0.1:8000/apicita/v1/posts/?format=json')
      .then((response) => {
        return response.json();
      })
      .then((empleados) => {
        this.setState({ empleados: empleados })
      })
  }

  render() {
    if (this.state.empleados.length > 0) {

      return (
        <div className="container-fluid">
          <PostList listado={this.state.empleados} />
        </div>
      )
    } else {
      return <p className="text-center">Cargando empleados...</p>
    }
  }

}


export default Posteos
