import axios from 'axios';
import React, {Component} from 'react';
import Header from './components/header/Header'


class App extends Component {
  state = {};

  componentDidMount() {
  }

  render() {
    return (
      <div className="App">
        <Header />
      </div>
    );
  }
}

export default App;
