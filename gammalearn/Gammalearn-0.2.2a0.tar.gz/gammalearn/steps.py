import torch


def training_step_gradnorm(experiment):
    """

    Parameters
    ----------
    experiment

    Returns
    -------

    """

    def training_step(engine, samples):
        """
        The training operations for one batch
        Returns
        -------

        """
        experiment.net.train()

        for _, optim in experiment.optimizers.items():
            if optim is not None:
                optim.zero_grad()

        # Load data
        images = samples['image'].to(experiment.device)
        labels = samples['label'].to(experiment.device)

        output = experiment.net(images)

        # Compute loss
        losses, loss_data = experiment.compute_loss(output, labels)

        weighted_losses = losses * experiment.compute_loss.weights
        loss = torch.sum(weighted_losses)

        # Compute gradients w.r.t. the parameters of the network
        loss.backward(retain_graph=True)

        experiment.compute_loss.zero_grad()

        # Compute the inverse training rate
        loss_ratio = losses / experiment.compute_loss.initial_losses.to(experiment.device)
        average_loss_ratio = loss_ratio.mean()
        inverse_training_rate = loss_ratio / average_loss_ratio

        # Compute the gradient norm of each task and the mean gradient norm
        gw_norms = []
        if hasattr(experiment.net, 'feature'):
            common_layer = getattr(experiment.net.feature, experiment.compute_loss.last_common_layer)
        else:
            common_layer = getattr(experiment.net, experiment.compute_loss.last_common_layer)
        for i, loss in enumerate(losses):
            gw = torch.autograd.grad(loss,
                                     common_layer.parameters(),
                                     retain_graph=True)[0]
            gw_norms.append(torch.norm(gw * experiment.compute_loss.weights[i]))
        gw_mean = torch.stack(gw_norms).mean().to(experiment.device)

        # Gradient target (considered as a constant term)
        grad_target = gw_mean * (inverse_training_rate**experiment.compute_loss.alpha)
        grad_target = grad_target.clone().detach().requires_grad_(False)
        # Gradnorm loss
        gradnorm_loss = torch.sum(torch.abs(torch.stack(gw_norms).to(experiment.device) - grad_target))

        experiment.compute_loss.weights.grad = torch.autograd.grad(gradnorm_loss, experiment.compute_loss.weights)[0]

        for _, optim in experiment.optimizers.items():
            if optim is not None:
                optim.step()

        # Normalize gradient weights
        experiment.compute_loss.weights.data = experiment.compute_loss.weights * (experiment.compute_loss.task_number / experiment.compute_loss.weights.sum())

        return output.data.cpu(), labels.data.cpu(), loss_data

    return training_step


def training_step_mt(experiment):
    """

    Parameters
    ----------
    experiment

    Returns
    -------

    """

    def training_step(engine, samples):
        """
        The training operations for one batch
        Returns
        -------

        """
        experiment.net.train()
        for _, optim in experiment.optimizers.items():
            if optim is not None:
                optim.zero_grad()

        # Load data as variable
        images = samples['image'].to(experiment.device)
        labels = samples['label'].to(experiment.device)

        output = experiment.net(images)

        # Compute loss
        loss, loss_data = experiment.compute_loss(output, labels)
        loss = torch.stack(loss).sum()
        if experiment.regularization is not None:
            loss += experiment.regularization['function'](experiment.net) * experiment.regularization['weight']
        loss.backward()
        for _, optim in experiment.optimizers.items():
            if optim is not None:
                optim.step()

        return output.data.cpu(), labels.data.cpu(), loss_data

    return training_step


def training_step_mt_gradient_penalty(experiment):
    """

    Parameters
    ----------
    experiment

    Returns
    -------

    """

    def training_step(engine, samples):
        """
        The training operations for one batch
        Returns
        -------

        """
        experiment.net.train()
        for _, optim in experiment.optimizers.items():
            if optim is not None:
                optim.zero_grad()

        # Load data as variable
        images = samples['image'].to(experiment.device)
        labels = samples['label'].to(experiment.device)

        images.requires_grad = True

        output = experiment.net(images)

        # Compute loss
        loss, loss_data = experiment.compute_loss(output, labels)
        loss = torch.stack(loss).sum()
        if experiment.regularization is not None:
            gradient_x = torch.autograd.grad(loss, images, retain_graph=True)[0]
            penalty = torch.mean((torch.norm(gradient_x.view(gradient_x.shape[0], -1), 2, dim=1) - 1) ** 2)
            loss += penalty * experiment.regularization['weight']
        loss.backward()
        for _, optim in experiment.optimizers.items():
            if optim is not None:
                optim.step()

        return output.data.cpu(), labels.data.cpu(), loss_data

    return training_step


def eval_step_mt(experiment):
    """

    Parameters
    ----------
    experiment

    Returns
    -------

    """
    def eval_step(engine, samples):
        """
        The validating operations for one batch
        Parameters
        ----------
        engine
        samples

        Returns
        -------

        """
        experiment.net.eval()
        with torch.no_grad():
            images = samples['image'].to(experiment.device)
            labels = samples['label'].to(experiment.device)

            output = experiment.net(images)
        # Compute loss and quality measures
            _, loss_data = experiment.compute_loss(output, labels)

            return output.data.cpu(), labels.data.cpu(), loss_data, samples['mc_energy'], samples['telescope'][:, 0:4]
    return eval_step


