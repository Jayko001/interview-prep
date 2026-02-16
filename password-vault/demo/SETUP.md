# Demo Setup

## Prerequisites
- [Docker](https://docs.docker.com/get-docker/) and Docker Compose
- [Tailscale](https://tailscale.com/) (for MagicDNS / `*.ts.net` domain)

## 1. Create a Tailscale domain

Ensure Tailscale is running and MagicDNS is enabled. Your machine will have a domain like `yourmachine.tail1234.ts.net`. For the vault, use a subdomain: `vault.tail1234.ts.net` (Tailscale supports multiple hostnames on one node).

## 2. Configure environment

Create a `.env` file in the `demo/` directory:

```env
# Generate with: openssl rand -base64 48
ADMIN_TOKEN=<your-generated-token>

# Your Tailscale domain (e.g., vault.tail1234.ts.net)
TAILSCALE_DOMAIN=vault.tail1234.ts.net
```

## 3. Update Caddyfile

Edit `Caddyfile` and replace the domain with yours so it matches `TAILSCALE_DOMAIN`:

```
vault.yourmachine.ts.net {
    tls internal
    ...
}
```

## 4. Start the stack

```bash
docker-compose up -d
```

## 5. Access the vault

Navigate to `https://<your-tailscale-domain>` (e.g., `https://vault.tail1234.ts.net`).

You’ll see a browser warning about the self-signed certificate — expected for this PoC. In production you’d use a valid cert (e.g. Let’s Encrypt). Proceed to accept the warning.

## 6. Admin panel (optional)

Visit `https://<your-tailscale-domain>/admin` and sign in with `ADMIN_TOKEN` to manage users, RBAC, and settings.

---

## Backup (optional)

To run a manual backup:

```bash
./scripts/backup.sh
```

Backups are written to `demo/backups/`.
