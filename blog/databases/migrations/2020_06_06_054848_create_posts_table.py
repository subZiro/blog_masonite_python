from orator.migrations import Migration


class CreatePostsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('posts') as table:
            table.increments('id')
            table.string('title')
            table.text('body')
            table.string('image')
            table.timestamps()

            table.integer('author_id').unsigned()
            table.foreign('author_id').references('id').on('users')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('posts')
