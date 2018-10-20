import axios from 'axios';
import React, {Component} from 'react';

import './Header.sass';


export default class Header extends Component {
  state = {
    moviepanels: [],
  }

  componentDidMount() {
    axios.get('http://localhost:8000/api/panels/')
      .then(res => {
        const moviepanels = res.data;
        this.setState({ moviepanels });
      })
      .catch(e => {
        console.log(e)
      })
  }

  render() {
    const moviepanels_list = this.state.moviepanels.map((moviepanel) => {
      return (
        <li className="nav-item dropdown" key={moviepanel.id}>
          <a className="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            {moviepanel.name}
          </a>
          <div className="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
            {moviepanel.moviegenres.map((moviegenre) =>
              <a className="dropdown-item" href="#" key={moviegenre.id}>{moviegenre.name}</a>
            )}
          </div>
        </li>
      );
    })

    return (
      <header className="main-header">
        <nav className="navbar navbar-expand-lg navbar-light bg-light">
          <a className="navbar-brand" href="#">Navbar</a>
          <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNavDropdown">
            <ul className="navbar-nav">
              <li className="nav-item active">
                <a className="nav-link" href="#">Home <span className="sr-only">(current)</span></a>
              </li>
              <li className="nav-item">
                <a className="nav-link" href="#">Features</a>
              </li>
              {moviepanels_list}
            </ul>
          </div>
        </nav>
      </header>
    )
  }
}
