---
layout: page
title: Neural surrogates for pathogen-importation forecasting
description: Making a global, coupled ODE model tractable for Bayesian inference and probabilistic forecasting.
importance: 1
category: research
---

## The problem

Forecasting pathogen importation across a connected world requires both mechanistic realism and repeated model evaluation. The underlying metapopulation model links 238 countries and territories through air and ground transportation, making direct likelihood-free inference computationally demanding.

## My contribution

I conceived and developed a mechanistically informed neural-surrogate methodology to test whether machine-learning approximations can preserve the useful behaviour of the coupled ODE model while reducing evaluation cost. I designed temporally conditioned surrogate architectures and comparative graph-attention and recurrent models that incorporate transportation-network and location-level features.

I built the end-to-end Python research pipeline: mechanistic simulation, parameter-space sampling, surrogate training, SMC-ABC inference, posterior uncertainty propagation, validation against observed first-case records, and computational benchmarking.

**Methods and tools:** Python, PyTorch, PyTorch Geometric, graph attention networks, LSTM/GRU models, SMC-ABC, ODE simulation, uncertainty quantification, spatiotemporal networks.

**Status:** Postdoctoral research; manuscript in preparation.
