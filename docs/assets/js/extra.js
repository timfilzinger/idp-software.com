// Make external links open in new tab
document.addEventListener('DOMContentLoaded', function() {
    const links = document.querySelectorAll('a[href^="http"]');
    links.forEach(function(link) {
        if (!link.href.includes('idp-software.com') && !link.href.includes('localhost')) {
            link.setAttribute('target', '_blank');
            link.setAttribute('rel', 'noopener noreferrer');
        }
    });
});