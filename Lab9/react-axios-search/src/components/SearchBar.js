import React from "react";

function SearchBar({ searchTerm, setSearchTerm }) {
return (
<div>
<input
type="text"
placeholder="Search users by name..."
value={searchTerm}
onChange={(e) => setSearchTerm(e.target.value)}
style={{
padding: "10px",
width: "250px",
borderRadius: "5px",
border: "1px solid gray",
}}
/>
</div>
);
}

export default SearchBar;
