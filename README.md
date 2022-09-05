# F`u`\*k S3

### What in the hell is this thing?
This is a simple cli-based tool to help you manage your S3 buckets.

### How do I use it?
If you do this.. `inv --list`

You'll get a list of all the tasks that are available in this task runner.
```
Available tasks:

  delete-bucket   Delete a bucket
  empty-bucket    Empty a bucket
  list-buckets    List all buckets
```
then if you run `inv the <task_name>` you'll get that task to run.

### Why?
I was tired of having to remember the aws cli commands to do simple things like list buckets, delete buckets, empty buckets, etc. So I made this.

### How do I use it?