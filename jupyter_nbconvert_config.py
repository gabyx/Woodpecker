c = get_config()
c.Application.log_level = 'DEBUG'
c.Exporter.preprocessors = ["jupyter_contrib_nbextensions.nbconvert_support.EmbedImagesPreprocessor"]
c.EmbedImagesPreprocessor.embed_images=True
c.NbConvertApp.export_format = "html_toc"
c.CodeFoldingPreprocessor.remove_folded_code=True
