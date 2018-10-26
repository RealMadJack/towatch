import axios from 'axios';
import React, {Component} from 'react';

import Page404 from './../404/Page404';
import './SignIn.sass';


export default class SignIn extends Component {
  state = {
    name: '',
    password: '',
  };

  handleChange = e => {
    if (e.target.name === 'name') {
      this.setState({
        name: e.target.value,
      });
    } else if (e.target.name === 'password') {
      this.setState({
        password: e.target.value,
      });
    }
  };

  handleSubmit = e => {
    e.preventDefault();
    console.log(this.state);
  };

  render() {
    return(
      <div className="container">
        <div className="row">
          <h1 className="col-12">Sign In:</h1>
          <form className="sign-form" onSubmit={this.handleSubmit}>
            <div className="form-field">
              <label htmlFor="validateAccountName">Account name</label>
              <input type="text"
                     name="name"
                     className="form-control is-valid"
                     id="validateAccountName"
                     onChange={this.handleChange}
                     placeholder="Account name" required />
              <div className="invalid-feedback">Please provide valid account name</div>
            </div>
            <div className="form-field">
              <label htmlFor="validatePassword">Password</label>
              <input type="text"
                     name="password"
                     className="form-control is-invalid"
                     id="validatePassword"
                     onChange={this.handleChange}
                     placeholder="Password" required />
              <div className="invalid-feedback">Please provide valid password</div>
            </div>
            <button className="btn btn-primary" type="submit">Submit form</button>
          </form>
        </div>
      </div>
    );
  }
}
