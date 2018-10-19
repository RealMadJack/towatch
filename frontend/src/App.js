import axios from 'axios';
import React, {Component} from 'react';
import './App.css';

class App extends Component {
  state = {
    api: [],
  };

  componentDidMount() {
    axios.get('http://localhost:8000/api/')
      .then(res => {
        console.log(res.data)
        const api = res.data;
        this.setState({ api });
      })
  }

  render() {
    return (
      <div className="App">
        <a href={ this.state.api['genres'] }>{ this.state.api['genres'] }</a>
      </div>
    );
  }
}

export default App;
