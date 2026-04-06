import React from "react";

function DataList({ data }) {
return (
<div style={{ marginTop: "20px" }}>
{data.length > 0 ? (
data.map((user) => (
<div
key={user.id}
style={{
border: "1px solid #ccc",
padding: "10px",
margin: "10px auto",
width: "300px",
borderRadius: "8px",
}}
>
<h3>{user.name}</h3>
<p>Email: {user.email}</p>
<p>Company: {user.company.name}</p>
</div>
))
) : (
<p>No results found</p>
)}
</div>
);
}

export default DataList;
