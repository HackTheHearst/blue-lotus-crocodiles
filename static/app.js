var entityMap = {
    "&": "&amp;",
    "<": "&lt;",
    ">": "&gt;",
    '"': '&quot;',
    "'": '&apos;'
};

function escapeHtml(string) {
    return String(string).replace(/[&<>"']/g, function (s) {
        return entityMap[s];
    });
}

function getImgUrl(blob, term) {
    term = term || 'OriginalJpeg';

    return 'https://dev.cspace.berkeley.edu/pahma_project/imageserver/blobs/' + blob + '/derivatives/' + term + '/content';
}