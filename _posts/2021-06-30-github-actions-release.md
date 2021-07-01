---
layout: post
title: How to upload assets to an existing Release in Github Actions
---

Summary: use `github.event.release.upload_url` as the upload URL for Release assets when triggering a workflow on a published GitHub Release.

We've been using travis-ci.org in a couple of repositories for some simple CI/CD workflows. [travis-ci.org](https://blog.travis-ci.com/2021-05-07-orgshutdown) shutdown on the 15th of June so we've needed to find a way to move these workflows over to a different service. I chose Github Actions because of its ease of use and integration in GitHub. It's capabilities seemed adequate for the simple workflows we needed. GitHub Actions are generally easy to setup if you follow the [documentation](https://docs.github.com/en/actions) but there was one part which I had more trouble figuring out. 

Our this particular repository is a command line application written in Python, which is distributed using GitHub Releases. After a PR with a new version is merged, we manually create a Release and let the CI/CD pipeline build the assets and upload them to the Release. With GitHub Actions, you specify your workflow as a sequence of steps, which contain your own code or one of many Actions pre-built by either GitHub or third parties. I didn't want to use a non-verified third party Action, so I was looking for an official one. GitHub has one called [upload-release-assets](https://github.com/actions/upload-release-asset) which seems to be doing exactly what I needed. It's repository is archived, however it's still usable. 

The question was how to find a the `upload_url` to specify where to upload the assets. The documentation only provides an example workflow which creates a Release by itself in the preceeding step using the [create-release action](https://github.com/actions/create-release) and then retrieves it using `steps.create_release.outputs.upload_url`.

I wanted this workflow to be triggered by us manually creating a Release and letting the workflow upload the built assets to this Release. Ahelpful [Stack Overflow answer](https://stackoverflow.com/questions/65521101/upload-url-for-githubs-upload-release-asset-action-when-the-trigger-is-a-releas) and double check with the [GitHub documentation](https://docs.github.com/en/developers/webhooks-and-events/webhooks/webhook-events-and-payloads#release) answer the question. 

To start a workflow when a Release is created, specify
```
on:
  release:
    types:
      - published
```
in your workflow yaml configuration. If you do that you can get the corresponding url by using `${{ github.event.release.upload_url }}` as the `upload_url`in your `upload-release-asset` step.



