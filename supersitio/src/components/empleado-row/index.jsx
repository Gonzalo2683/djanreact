import React from 'react'

class PostItem extends React.Component {

  render() {
    return(
      <li className="media">

        <div className="media-body">
          <h4>{this.props.titulo}</h4>
          <p>
            {this.props.contenido} &nbsp;
          </p>
        </div>
        <hr/>
      </li>
    )
  }
}

export default PostItem
