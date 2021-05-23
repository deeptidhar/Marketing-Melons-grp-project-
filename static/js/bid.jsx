function BidForm(props){
    const [bidAmount, setBidAmount] = React.useState(0);
    
    function handleSubmit(evt){
      evt.preventDefault();
      console.log(bidAmount);
      fetch('/api/bid', 
        {method: 'POST', 
        body: JSON.stringify({'listingId': 10, 'userId': 1, 'bidAmount': bidAmount}), 
        headers: {'Content-type': 'application/json'} //needed so the server knows where to get the values out from
        })
      .then(response => response.json())
      .then(data => {
        console.log(data);
          alert(data.status);
      })
    }
  
    return (
      <form onSubmit={(evt) => {handleSubmit(evt)}}>
        <label>Enter a dollar amount</label>
        $<input type="number" name="currency" min="0" max="9999" step="0.01" size="4"
                onChange={ evt => { setBidAmount(evt.target.value) } } />
        <input type='submit' />
      </form>
      )
  }