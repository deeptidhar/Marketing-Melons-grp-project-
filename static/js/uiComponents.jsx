/////////////////////////////////////////////////////////////
function Homepage(props) {
  return (
    <div id="home-banner" className="row">
      <div className="col">
        <h1>BitMelon</h1>
        <p className="lead">Marketplace for melons.</p>
      </div>
    </div>
  );
}

function PageContainer(props) {
  const { children, className, title, ...rest } = props;
  return (
    <ReactRouterDOM.BrowserRouter>
      <h1>{title}</h1>
      <div {...rest} className={`row ${className || ""}`}>
        {children}
      </div>
    </ReactRouterDOM.BrowserRouter>
  );
}
/////////////////////////////////////////////////////////////
function MarketplacePage(props) {
  const { listings } = props;
  const listingCards = [];

  for (const listing of Object.values(listings)) {
    const listingCard = (
      <ListingCard
        category={listing.category}
        color={listing.color}
        description={listing.description}
        endDate = {listing.end_date}
        imgUrl = {listing.image_url}
        isSeedless = {listing.is_seedless}
        key={listing.listing_id}
        name={listing.name}
        seller={listing.seller}
        startPrice={listing.start_price}
        topBid = {listing.top_bid}
        topBidder = {listing.top_bidder}
      />
    );
    listingCards.push(listingCard);
  }

  return (
    <PageContainer title="Marketplace" id="marketplace">
      <div className="col-12 col-md-9 d-flex flex-wrap">{listingCards}</div>
    </PageContainer>
  );
}
/////////////////////////////////////////////////////////////
function ListingCard(props) {
  const { category, color, description, endDate, imgUrl, isSeedless,
          name, seller, startPrice, topBid, topBidder } = props;

  return (
    <div className="card melon-card">
        <img src={imgUrl} className="card-img-top" />
      <div className="card-title">
        <h3>{name}</h3>
        <h4><i>{category}</i></h4>
        <p>Description: {description}</p>
        <h6>seller: {seller}</h6>
      </div>
      <div className="card-body pt-0 container-fluid">
        <div className="row">
          <div className="col-12 col-lg-6">
            <ul>
              <li>color: {color}</li>
              <li>seeds: {isSeedless.toString()}</li>
              <li>min price: ${startPrice.toFixed(2)}</li>
            </ul>
          </div>
          <div className="col-12 col-lg-6">
            <ul>
              <li>sale ends: {endDate}</li>
            </ul>
          </div>
          <div className="card-body pt-0 container-fluid">
            <span className="lead price d-inline-block">
              Top Bid: ${topBid == undefined ? 0 : topBid.toFixed(2)}
            </span>
            <p>Top Bidder: {topBidder}</p>
            <button
                className="btn btn-sm btn-success d-inline-block"
                onClick={() => {}}
              >
                Place Bid
              </button>
          </div>
        </div>
      </div>
    </div>
  );
}
/////////////////////////////////////////////////////////////
function Navbar(props) {
  const { logo, brand, children, className } = props;

  const navLinks = children.map((el, i) => {
    return (
      <div key={i} className="nav-item">
        {el}
      </div>
    );
  });

  return (
    <nav className={`navbar ${className || ""}`}>
      <ReactRouterDOM.Link
        to="/"
        className="havbar-brand d-flex justify-content-center"
      >
        <img src={logo} height="30" />
        <span>{brand}</span>
      </ReactRouterDOM.Link>

      <section className="d-flex justify-content-center">{navLinks}</section>
    </nav>
  );
}
/////////////////////////////////////////////////////////////
function Loading() {
  return (
    <div className="loading-box">
      <img src="static/img/watermelon-loading.png" alt="" />
      <div>Loading...</div>
    </div>
  );
}
/////////////////////////////////////////////////////////////
