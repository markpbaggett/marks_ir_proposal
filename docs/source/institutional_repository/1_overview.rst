Institutional Repository Overview
=================================

As described in `Overall Infrastructure, Preservation, and Interoperability <0_Repository_Infrastructure.rst>`_, we
intend to have our institutional repository in a single, Hyrax-based application. Historically, we've kept our institutional
repository and digital collections repository as they serve different use cases, have different use cases, and have very
different requirements.  While we want these applications to be separate, we are not opposed to use the same Fedora
repository or search index. If we were to use the same search index, we would require that we could limit results to one
application as a default search.

.. image:: ../images/overview.png

While we are not opposed to ActiveFedora initially, we see value in our applications ultimately interacting with Fedora,
the search, index, and other services with `valkyrie <https://github.com/samvera/valkyrie>`_.

Finally, as stated in `Overall Infrastructure, Preservation, and Interoperability <0_Repository_Infrastructure.rst>`_,
we are not opposed to going live with a new institutional repository platform with Fedora 4 or Fedora 5 as long as we have
a road map up front for moving to Fedora 6.  For more information about reasons for this, see the document above.