from textgenrnn import textgenrnn

textgen = textgenrnn()
textgen.train_from_file('all_posts_txt', num_epochs=100)
textgen.generate(10)
textgen.save()
textgen.train_from_file('all_posts_txt', num_epochs=200)
textgen.generate(10)
textgen.save('Generator_weights_200_epochs')
