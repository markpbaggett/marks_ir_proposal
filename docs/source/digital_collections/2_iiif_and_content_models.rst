IIIF and Content Models
-----------------------

It is our intent to serve content via the IIIF presentation API in our next repository application.  The IIIF presentation
API provides a uniform method for us to to serve data regardless of content model. It also allows us to focus our efforts
around a single specification and viewer for display.

For each content model, we will develop a mapping between our descriptive and structural metadata to a IIIF presentation
manifest. The manifest will be read by the viewer and display the object accordingly. The manifest will include minimal
descriptive metadata. It will also

Doing this will allows us to control various things.  For audio visual content, we will be able to control the display
of structures and ranges and add transcripts for closed captioning. For books and other compound objects, we will be able
to control viewing direction and OCR application.

Utilizing the presentation API allows researchers and other users to annotate our objects.  It will also allow us to pull
content into other applications for display as appropriate.

Initial recipes regarding how we imagine our IIIF models can be found in our `cookbook <https://utk-iiif-cookbook.readthedocs.io/en/latest/>`_.

Our current content models are described in our `Digital Collections Content Models documentation <https://utk-dc-content-models.readthedocs.io/en/latest/>`_.
We intend to work closely with vendors and contractors to make decisions about how these will work in our next system.
