import React from 'react'
import PostItem from '../empleado-row/index'

class PostList extends React.Component {

  render() {
    return (
      <div className="container-fluid">
        <ul className="media-list">
          {
            this.props.listado.map((empleado) => {
              return <PostItem key={ empleado.id } contenido={empleado.contenido} name={ empleado.autor } />
            })
          }
        </ul>
      </div>
    )
  }
}


export default PostList





