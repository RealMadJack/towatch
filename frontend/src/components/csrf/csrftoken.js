import React from 'react';
import Cookies from 'js-cookie';


export const csrftoken_str = Cookies.get('csrftoken');
console.log(csrftoken_str)


const CSRFToken = () => {
  return (
      <input type="hidden" name="csrfmiddlewaretoken" value={csrftoken_str} />
  );
};
export default CSRFToken;
