<h2>Watching Github Projects</h2>
<div>Owner: ${owner}</div>
<ul>
    % for proj in projects:
        <li>${proj}</li>
    % endfor
</ul>
