
            else:
                post=Posts.query.filter_by(sno=sno).first() 
                post.title=box_title
                post.tline=tline
                post.slug=slug
                post.content=content
                post.img_file=img_file                 
                post.date=date